def hospital_expert_system():
    print("Welcome to QuickMed Expert System!")
    print("Answer the following questions with yes/no.\n")

    # Define rules: condition -> list of symptoms
    rules = {
        "Common Cold": ["cough", "runny nose", "sore throat", "fever"],
        "Flu": ["fever", "headache", "body ache", "fatigue", "cough"],
        "COVID-19": ["fever", "cough", "fatigue", "loss of taste", "shortness of breath"],
        "Allergy": ["sneezing", "runny nose", "itchy eyes"],
        "Food Poisoning": ["vomiting", "diarrhea", "stomach pain", "fever"]
    }

    # Collect patient's symptoms
    patient_symptoms = []

    # Ask about common symptoms
    common_symptoms = set(sum(rules.values(), []))  # flatten list of symptoms
    for symptom in common_symptoms:
        answer = input(f"Do you have {symptom}? (y/n): ").strip().lower()
        if answer == "y":
            patient_symptoms.append(symptom)

    # Evaluate rules
    matched_conditions = []
    for condition, symptoms in rules.items():
        match_count = sum(1 for s in symptoms if s in patient_symptoms)
        if match_count >= len(symptoms) // 2:  # threshold: half of symptoms match
            matched_conditions.append(condition)

    # Output results
    if matched_conditions:
        print("\nBased on your symptoms, possible conditions are:")
        for cond in matched_conditions:
            print("-", cond)
        print("\nPlease consult a medical professional for confirmation and treatment.")
    else:
        print("\nNo clear condition could be determined from your symptoms.")
        print("If you feel unwell, please consult a doctor.")

# Run the expert system
hospital_expert_system()
