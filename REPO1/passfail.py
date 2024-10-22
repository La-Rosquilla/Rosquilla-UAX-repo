# Function to determine pass or fail status
def evaluate_student_pass_fail(exam_score, total_classes, attended_classes):
    # Calculate the attendance percentage
    attendance_percentage = (attended_classes / total_classes) * 100
    
    # Check if both the exam score and attendance criteria are met
    if exam_score >= 70 and attendance_percentage >= 80:
        return "Pass"
    else:
        return "Fail"

# Main program
def main():
    # User input for exam score, total classes, and attended classes
    exam_score = float(input("Enter the exam score (out of 100): ") or 75)
    total_classes = int(input("Enter the total number of classes: ") or 40)
    attended_classes = int(input("Enter the number of classes attended: ") or 32)

    # Call the function to evaluate pass/fail
    result = evaluate_student_pass_fail(exam_score, total_classes, attended_classes)

    # Display the result
    print(f"Student's Result: {result}")

# Run the program
if __name__ == "__main__":
    main()
