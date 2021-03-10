-- Create index idx_name_first
-- on the names table and the 1st letter of the name
CREATE INDEX idx_name_first ON names ( name(1) );
