class EmailService:

    def _connect(self):
        print("Connecting to email server")

    def _authenticate(self):
        print("Authenticting")

    def send_email(self):
        self._connect()
        self._authenticate()
        print("Send the email")
        self._disconnect()

    def _disconnect(self):
        print("Disconnecting from Email Server")


email = EmailService()
email.send_email()
