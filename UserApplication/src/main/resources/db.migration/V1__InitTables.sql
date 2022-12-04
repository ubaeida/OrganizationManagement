CREATE TABLE `organizationmanagement`.`user`
(
    `id`       BIGINT       NOT NULL AUTO_INCREMENT,
    `email`    VARCHAR(255) NULL,
    `gender`   INT NULL,
    `name`     VARCHAR(255) NULL,
    `type`     INT NULL,
    `username` VARCHAR(255) NULL,
    `password` VARCHAR(255) NOT NULL,
    PRIMARY KEY (`id`),
    UNIQUE INDEX `username_UNIQUE` (`username` ASC) VISIBLE
);
