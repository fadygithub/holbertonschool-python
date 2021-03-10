-- Create index idx_name_first_score for the table names
-- in addition to the first letter of name and score
CREATE INDEX idx_name_first_score ON names ( name(1), score );
