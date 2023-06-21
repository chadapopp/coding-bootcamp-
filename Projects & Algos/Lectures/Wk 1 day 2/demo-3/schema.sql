CREATE TABLE users (
	id INT NOT NULL AUTO_INCREMENT,
	email VARCHAR(255) NOT NULL,
	user_name VARCHAR(255) NOT NULL,
	password VARCHAR(255) NOT NULL,
	created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	PRIMARY KEY (id)
);


CREATE TABLE files (
	id INT NOT NULL AUTO_INCREMENT,
	user_id INT NOT NULL,
	file_name VARCHAR(255) NOT NULL,
	size INT NOT NULL,
	extension VARCHAR(40) NOT NULL,
	created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	PRIMARY KEY (id),
	FOREIGN KEY (user_id) REFERENCES users(id) ON UPDATE CASCADE ON DELETE CASCADE
);