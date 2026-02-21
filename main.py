##Code 
print("=== FIX FLOW ===")

def classify_ticket(text):
    text = text.lower()

    if "password" in text or "login" in text:
        return "Account Issue"

    elif "payment" in text or "money" in text or "refund" in text:
        return "Payment Issue"

    elif "error" in text or "crash" in text or "not working" in text:
        return "Technical Issue"

    else:
        return "General Issue"


def give_solution(category):
    if category == "Account Issue":
        return "Please reset your password or check login details."

    elif category == "Payment Issue":
        return "Please check transaction status. Refund takes 3 to 5 days."

    elif category == "Technical Issue":
        return "Try restarting the app or reinstalling."

    else:
        return "Our team will contact you soon."


def check_escalation(text):
    text = text.lower()
    if "urgent" in text or "human" in text or "help" in text:
        return True
    return False


while True:
    ticket = input("\nEnter customer ticket (or type exit): ")

    if ticket.lower() == "exit":
        print("Thank you for using Smart Ticket Chatbot. Goodbye!")
        break

    category = classify_ticket(ticket)
    print("Issue Type:", category)

    if check_escalation(ticket):
        print("⚠ Escalating to human support...")
        print("We will resolve your issue as soon as possible. If you have further issues, please submit a new request.")
    else:
        print("Solution:", give_solution(category))
        print("We will solve your problem shortly. If you have further issues, please submit a new request.")
