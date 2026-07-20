import os


def generate_invitations(template, attendees):
    """
    Generate personalized invitation files from a template and attendees list.
    """
    # Check input types
    if not isinstance(template, str):
        print(f"Error: Invalid template type. Expected string, got {type(template).__name__}")
        return
    
    if not isinstance(attendees, list):
        print(f"Error: Invalid attendees type. Expected list, got {type(attendees).__name__}")
        return
    
    # Check if all items in attendees are dictionaries
    if attendees and not all(isinstance(item, dict) for item in attendees):
        print("Error: Not all items in attendees list are dictionaries")
        return
    
    # Check if template is empty
    if not template or template.strip() == "":
        print("Template is empty, no output files generated.")
        return
    
    # Check if attendees list is empty
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        # Create a copy of the template for processing
        output_content = template
        
        # Define placeholders to replace
        placeholders = ["name", "event_title", "event_date", "event_location"]
        
        # Replace each placeholder with the corresponding value
        for placeholder in placeholders:
            value = attendee.get(placeholder, "N/A")
            # Handle None values by replacing with "N/A"
            if value is None:
                value = "N/A"
            # Replace the placeholder with the value
            output_content = output_content.replace(f"{{{placeholder}}}", str(value))
        
        # Write to output file
        output_filename = f"output_{index}.txt"
        try:
            with open(output_filename, 'w') as file:
                file.write(output_content)
            print(f"Generated {output_filename}")
        except IOError as e:
            print(f"Error writing to {output_filename}: {e}")
