#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

class Message {
private:
    string str;
    int index;
public: 
    Message() {}
    Message(string t, int i) {
        str = t;
        index = i;
    }
    int getindex() {
        return index;
    }
    const string& get_text() {
        return str;
    }
    bool operator<(Message m2) {
        if (index < m2.getindex())
            return true;
        return false;
    }
};

class MessageFactory {
private:
    static int count;
public:
    MessageFactory() {}
    Message create_message(const string& text) {
        count += 1;
        Message m(text, count);
        return m;
    }
};

int MessageFactory::count = 0;

class Recipient {
public:
    Recipient() {}
    void receive(const Message& msg) {
        messages_.push_back(msg);
    }
    void print_messages() {
        fix_order();
        for (auto& msg : messages_) {
            cout << msg.get_text() << endl;
        }
        messages_.clear();
    }
private:
    void fix_order() {
        sort(messages_.begin(), messages_.end());
    }
    vector<Message> messages_;
};

class Network {
public:
    static void send_messages(vector<Message> messages, Recipient& recipient) {
    // simulates the unpredictable network, where sent messages might arrive in unspecified order
        random_shuffle(messages.begin(), messages.end());         
        for (auto msg : messages) {
            recipient.receive(msg);
        }
    }
};

int main() {
    MessageFactory message_factory;
    Recipient recipient;
    vector<Message> messages;
    string text;
    while (getline(cin, text)) {
        messages.push_back(message_factory.create_message(text));
    }
    Network::send_messages(messages, recipient);
    recipient.print_messages();
}
