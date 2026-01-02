def route_payment(event):
    metadata = event["data"].get("metadata", {})
    service_type = metadata.get("service_type")

    if not service_type:
        raise ValueError("Missing service_type in metadata")

    if service_type == "exam_token":
        from orders.handlers import handle_exam_token_payment
        handle_exam_token_payment(event)

    elif service_type == "service_booking":
        from service_section.Payment.handlers import handle_service_payment
        handle_service_payment(event)

    else:
        raise ValueError(f"Unknown service_type: {service_type}")
