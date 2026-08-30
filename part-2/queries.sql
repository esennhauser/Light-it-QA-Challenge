-- List all appointments belonging to the current patient,
-- including the doctor's name, date, time slot, and status,
-- ordered from the most recent appointment to the oldest.
SELECT
    a.appointment_date,
    a.time_slot,
    d.first_name || ' ' || d.last_name AS doctor_name,
    a.status
FROM appointments AS a
JOIN doctors AS d
    ON a.doctor_id = d.id
WHERE a.patient_id = 70
ORDER BY a.appointment_date DESC;

-- List all doctors and the total number of appointments assigned to each doctor,
-- including doctors who have no appointments.
SELECT
    d.id AS doctor_id,
    d.first_name || ' ' || d.last_name AS doctor_name,
    COUNT(a.id) AS appointment_count
FROM doctors AS d
LEFT JOIN appointments AS a
    ON d.id = a.doctor_id
GROUP BY
    d.id,
    d.first_name,
    d.last_name
ORDER BY appointment_count DESC, doctor_name;

-- Identify future appointments assigned to doctors who are currently inactive,
-- including the doctor name, appointment date, appointment status, and patient name.
SELECT
    d.first_name || ' ' || d.last_name AS doctor_name,
    a.appointment_date,
    a.status AS appointment_status,
    u.first_name || ' ' || u.last_name AS patient_name
FROM appointments AS a
JOIN doctors AS d
    ON a.doctor_id = d.id
JOIN users AS u
    ON a.patient_id = u.id
WHERE a.appointment_date > CURRENT_DATE
  AND d.is_active = FALSE
ORDER BY a.appointment_date;

-- Identify scheduling conflicts where the same doctor has more than one
-- appointment assigned for the same date and time slot.
-- The count shows how many appointments are involved in each conflict.
-- Cancelled appointments are excluded because they should no longer occupy a doctor's time slot.
SELECT
    d.first_name || ' ' || d.last_name AS doctor_name,
    a.appointment_date,
    a.time_slot,
    COUNT(*) AS appointment_count
FROM appointments AS a
JOIN doctors AS d
    ON a.doctor_id = d.id
where a.status != 'cancelled'
GROUP BY
    d.id,
    d.first_name,
    d.last_name,
    a.appointment_date,
    a.time_slot
HAVING COUNT(*) > 1
ORDER BY
    a.appointment_date DESC,
    doctor_name;


-- Calculate the total revenue collected by each doctor from paid payments,
-- including each doctor's percentage of the overall collected revenue.
WITH doctor_revenue AS (
    SELECT
        d.id AS doctor_id,
        d.first_name || ' ' || d.last_name AS doctor_name,
        SUM(p.amount) AS total_revenue
    FROM doctors AS d
    JOIN appointments AS a
        ON d.id = a.doctor_id
    JOIN payments AS p
        ON a.id = p.appointment_id
    WHERE p.status = 'paid'
    GROUP BY
        d.id,
        d.first_name,
        d.last_name
)
SELECT
    doctor_id,
    doctor_name,
    total_revenue,
    ROUND(
        total_revenue / NULLIF(SUM(total_revenue) OVER (), 0) * 100,
        2
    ) AS percentage_of_total
FROM doctor_revenue
ORDER BY total_revenue DESC;

