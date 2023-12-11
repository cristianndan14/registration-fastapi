CREATE TABLE `patient` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `created_at` TIMESTAMP NOT NULL,
    `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    `is_deleted` BOOLEAN NOT NULL DEFAULT false,
    `uuid` CHAR(36) NOT NULL,
    `name` VARCHAR(100) NOT NULL,
    `email` VARCHAR(255) NOT NULL,
    `address` VARCHAR(200) NOT NULL,
    `phone_number` VARCHAR(20) NOT NULL,
    `photo_url` VARCHAR(200) NOT NULL,
    CONSTRAINT `patient_unique_uuid` UNIQUE (`uuid`),
    CONSTRAINT `patient_unique_email` UNIQUE (`email`)
);