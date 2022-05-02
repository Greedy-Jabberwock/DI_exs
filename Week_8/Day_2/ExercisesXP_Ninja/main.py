class Phone:
    border = '--------------------------------------------'

    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.call_history = []
        self.messages = []

    def call(self, other):
        outcome_call = f'Abonent {self.phone_number} called ' \
                       f'to abonent {other.phone_number}'
        self.call_history.append(outcome_call)
        other.call_history.append(outcome_call)

    def show_call_history(self):
        print(self.border)
        print('Calls: history')
        for x in self.call_history:
            print(f'\t{x}')
        print(self.border)

    def send_message(self, other, message):
        message_item = {'to': other.phone_number,
                        'from': self.phone_number,
                        'content': message}
        self.messages.append(message_item)
        other.messages.append(message_item)

    def show_ongoing_messages(self):
        print(self.border)
        print(f'Ongoing messages:')
        for message in self.messages:
            if message['from'] == self.phone_number:
                print(f'\t{message}')
        print(self.border)

    def show_incoming_messages(self):
        print(self.border)
        print(f'Incoming messages:')
        for message in self.messages:
            if message['from'] != self.phone_number:
                print(f'\t{message}')
        print(self.border)

    def show_messages_from(self, other):
        print(self.border)
        print(f'Messages from {other.phone_number}:\n')
        for message in self.messages:
            if message['from'] == other.phone_number:
                print(f'\t{message}')
        print(self.border)


jack = Phone('0552898888')
daniel = Phone('9161148679')
lisa = Phone('798-24-5556-21')
jack.call(lisa)
jack.call(daniel)
daniel.call(jack)
jack.show_call_history()
jack.send_message(lisa, 'Hello!')
jack.show_ongoing_messages()
lisa.send_message(jack, 'Fine. See you tomorrow?')
lisa.show_call_history()
lisa.show_incoming_messages()
daniel.send_message(jack, 'What\'s up, bro?')
jack.show_messages_from(daniel)
