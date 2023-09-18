-- Create a sample table
CREATE TABLE IF NOT EXISTS devops_backend_user (
    id int PRIMARY KEY,
    username VARCHAR(200) UNIQUE NOT NULL,
    email VARCHAR(200) UNIQUE NOT NULL,
    first_name VARCHAR(200) NOT NULL,
    last_name VARCHAR(200) NOT NULL
);

-- Insert some sample data
INSERT INTO devops_backend_user (id, username, email, first_name, last_name) VALUES
(1, 'dnaby', 'dnaby@eept.sn', 'Mouhamadou Naby', 'DIA'),
(2, 'wadess', 'wadess@eept.sn', 'Serigne Saliou', 'WADE');
