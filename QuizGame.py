#!/usr/bin/env python3
# A fun  quiz game about cybersecurity knowledge

# Prompt user to enter their name and store it after removing any extra whitespace
Player_name = input("Enter your name: ").strip()
print(f"Hello, {Player_name}! Welcome to the Cyber Security Quiz! \n")

def start_quiz():
    """Function to display the quiz results when called"""
    print(f"\nYour total score is: {total_score}")
    print(f"\nCorrect answers: {correct_answers}")
    print(f"\nWrong answers: {wrong_answers}")

# Initialize score counters
total_score = 0
correct_answers = 0
wrong_answers = 0

# Define the quiz questions, options, and answers as a list of dictionaries
quiz = [
    {
        "Question": "What is the primary purpose of a firewall?",
        "Options": [
            "A: To encrypt user data",
            "B: To detect malware on a computer",
            "C: To block unauthorized access to or from a network",
            "D: To manage user passwords"
        ],
        "Answer": "C. To block unauthorized access to or from a network"
    },
    {
        "Question": "Which of the following is an example of a strong password?",
        "Options": [
            "A: password123",
            "B: John2020",
            "C: M$kL9@r!2#zP",
            "D: qwerty"
        ],
        "Answer": "C. M$kL9@r!2#zP"
    },
    {
        "Question": "Phishing attacks are primarily aimed at",
        "Options": [
            "A: Infecting systems with ransomware",
            "B: Physically stealing computers",
            "C: Tricking users into revealing personal information",
            "D: Overloading websites with traffic"
        ],
        "Answer": "C. Tricking users into revealing personal information"
    },
    {
        "Question": "Which of these is a form of malware that locks or encrypts a victim's files until a ransom is paid?",
        "Options": [
            "A: Adware",
            "B: Ransomware",
            "C: Spyware",
            "D: Trojan"
        ],
        "Answer": "B. Ransomware"
    },
    {
        "Question": "What does the principle of 'least privilege' refer to in cybersecurity?",
        "Options": [
            "A: Users should have only the access necessary to perform their job functions.",
            "B: All users should have administrative access.",
            "C: Users should be allowed to install any software they want.",
            "D: Access rights should be granted based on seniority."
        ],
        "Answer": "A. Users should have only the access necessary to perform their job functions."
    },
    {
        "Question": "What is the role of encryption in cybersecurity?",
        "Options": [
            "A: To protect data confidentiality",
            "B: To ensure data integrity",
            "C: To provide authentication",
            "D: All of the above"
        ],
        "Answer": "D. All of the above"
    },
    {
        "Question": "What is a zero-day vulnerability?",
        "Options": [
            "A: A malware that activates after 24 hours",
            "B: A vulnerability that has been patched already",
            "C: A newly discovered vulnerability that is not yet known to the software vendor",
            "D: A virus with no known origin"
        ],
        "Answer": "C. A newly discovered vulnerability that is not yet known to the software vendor"
    }
]

# Dictionary containing security tips corresponding to each wrong question  user gets
security_tips = {
    0: "A firewall helps prevent unauthorized access. Always keep it enabled.",
    1: "Strong passwords are long and use symbols, numbers, and upper/lowercase letters.",
    2: "Never click unknown links or attachments; phishing attacks trick users into giving away info.",
    3: "Ransomware encrypts your data. Always backup files and avoid suspicious downloads.",
    4: "Only give users the access they need. 'Least privilege' reduces damage from attacks.",
    5: "Encryption secures your data during transmission. Always enable HTTPS and device encryption.",
    6: "Zero-day vulnerabilities are dangerous. Keep systems updated with patches."
}

# Initialize question counter
i = 0

# Loop through all quiz questions
while i < len(quiz):
    # Print the current question
    print(quiz[i]["Question"])
    
    # Print all options for the current question
    for Option in quiz[i]["Options"]:
        print(Option)
    
    # Loop to handle user input and validation
    while True:
        # Get user's answer or allow them to quit
        answer = input("\nEnter your answer or type 'quit' to exit: ")
        
        # Check if user wants to quit
        if answer.strip().lower() == "quit":
            print("Quiz ended by user.")
            exit()  # Exit the program
        
        # Validate input is A, B, C, or D
        if answer not in ["a", "b", "c", "d"]:
            print("Please enter a valid answer: A, B, C, or D.")
            continue  # Skip to next iteration if invalid
        
        # Check if answer is correct (compare with the first character of the stored answer)
        elif answer.strip().lower() == quiz[i]["Answer"].split(".")[0].strip().lower():
            print("Correct! ✅")
            total_score += 5  # Add to score
            correct_answers += 1  # Increment correct counter
        else:
            # Handle incorrect answer
            print(f" \nIncorrect. The correct answer is: {quiz[i]['Answer']} \n")
            print(f"Security Tip: {security_tips[i]} \n")  # Show relevant security tip
            wrong_answers += 1  # Increment wrong counter
        break  # Exit the input validation loop
    
    # Move to next question
    i += 1

# After all questions are answered, show the final results
start_quiz()
