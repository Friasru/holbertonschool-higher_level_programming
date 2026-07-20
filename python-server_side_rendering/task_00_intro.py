import os


def generate_invitations(template, attendees):
    """
    Generate personalized invitation files from a template
    """
    if not isinstance(template, str):
        print(f"Error: Invalid template type. Expected string, got {type(template).__name__}")
        return

    if not isinstance(attendees, list):
        print(f"Error: Invalid attendees type. Expected list, got {type(attendees).__name__}")
        return

    if attendees and not all(isinstance(item, dict) for item in attendees):
        print(f"Error: Not all items in attendees list are dictionaries")
        return
    
    if not template or template.strip() == "":
        print("Template is empty, not output files generated.")
        return
    
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    for index, attendee in enumerate(attendees, start=1):

        output_content = template

        placeholders = ["name", "event_title", "event_date", "event_location"]


        for placeholder in placeholders:
            value = attendee.get(placeholder, "N/A")

            if value is None:
                value = "N/A"

                output_content = output_content.replace(f"{{{placeholder}}}", str(value))

            output_filename = f"output{index}".txt
            try:
                with open(output_filename, 'w') as file:
                    file.write(output_content)
                print(f"Generated {output_filename}")
            except IOError as e:
                print(f"Error writing to {output_filename}: {e}")
