show privileges;
-- grant all the privileges
grant all privileges on clauses.* to userB; 
-- revoke all the privileges 
revoke all privileges on clauses.* from userB;
-- giving to access on specific table only
grant all privileges on clauses.emp2 to userB;
-- revoke all the privileges
revoke all privileges on clauses.emp2 from userB;
-- giving to access on specific task only
grant select,update  on clauses.emp2 to userB;
-- revoke  the privileges
revoke select,update  on clauses.emp2 from userB;