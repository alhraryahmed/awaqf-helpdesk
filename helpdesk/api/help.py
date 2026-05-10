import frappe

@frappe.whitelist(allow_guest=True)
def create_ticket(subject, description, rustdesk_id, rustdesk_password, device_name):

    doc = frappe.get_doc({
        "doctype": "HD Ticket",
        "subject": subject,
        "description": description,
        "rustdesk_id": rustdesk_id,
        "rustdesk_password": rustdesk_password,
        "custom_device_name": device_name,
        "status": "Open"
    })

    doc.insert(ignore_permissions=True)
    frappe.db.commit()

    return {"status": "success", "ticket": doc.name}