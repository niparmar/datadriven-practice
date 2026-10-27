select session_id,user_id, session_duration_sec from user_sessions where DATE_FORMAT(session_start ,'%Y') = '2026' and session_duration_sec < 100



--select * from user_sessions where session_duration_sec < 100
