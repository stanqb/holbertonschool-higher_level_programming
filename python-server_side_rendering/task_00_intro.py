def generate_invitations(template, attendees):
    """
    Generates personalized invitation files from a template and a list of
    attendees.

    Args:
        template (str): The template with placeholders {name}, {event_title},
                        etc.
        attendees (list): List of dictionaries containing attendee data
    """
    # Check template type
    if not isinstance(template, str):
        print(f"Error: template must be a string, not "
              f"{type(template).__name__}")
        return

    # Check attendees type
    if not isinstance(attendees, list):
        print(f"Error: attendees must be a list, not "
              f"{type(attendees).__name__}")
        return

    # Check if all items in attendees are dictionaries
    if attendees and not all(
        isinstance(attendee, dict) for attendee in attendees
    ):
        print("Error: all items in attendees must be dictionaries")
        return

    # Check if template is empty
    if not template:
        print("Template is empty, no output files generated.")
        return

    # Check if attendees is empty
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for i, attendee in enumerate(attendees, 1):
        invitation = template

        # Replace placeholders
        placeholders = [
            "name", "event_title", "event_date", "event_location"
        ]
        for placeholder in placeholders:
            value = attendee.get(placeholder)
            # Replace None or missing values with "N/A"
            if value is None:
                value = "N/A"
            invitation = invitation.replace(f"{{{placeholder}}}", str(value))

        # Write output file
        output_filename = f"output_{i}.txt"
        with open(output_filename, 'w') as file:
            file.write(invitation)
