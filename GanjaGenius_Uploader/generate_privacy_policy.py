from datetime import datetime

privacy_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Privacy Policy</title>
</head>
<body>
    <h1>Privacy Policy for {company_name}</h1>
    <p>Effective Date: {effective_date}</p>
    <p>{company_name} ("we", "our", or "us") is committed to protecting your privacy. This Privacy Policy explains how we collect, use, disclose, and safeguard your information when you use our service, GanjaGenius ("the Service"). Please read this policy carefully to understand our views and practices regarding your personal data.</p>
    
    <h2>Information We Collect</h2>
    <p>We may collect the following types of information:</p>
    <ul>
        <li>Personal Information: We collect your name, email address, and other contact details when you interact with our Service.</li>
        <li>Usage Data: We collect information on how you use our Service, including but not limited to your interactions, preferences, and other engagement activities.</li>
    </ul>
    
    <h2>How We Use Your Information</h2>
    <p>We use the collected information to:</p>
    <ul>
        <li>Provide, operate, and maintain the Service.</li>
        <li>Improve, personalize, and expand our offerings.</li>
        <li>Communicate with you, including customer service, updates, and other information relating to the Service.</li>
    </ul>
    
    <h2>Disclosure of Your Information</h2>
    <p>We may share your information in the following situations:</p>
    <ul>
        <li>With service providers and partners to provide and maintain our Service.</li>
        <li>When required by law or legal processes.</li>
        <li>In connection with a business transfer, such as a merger or acquisition.</li>
    </ul>
    
    <h2>Security of Your Information</h2>
    <p>We take appropriate technical and organizational measures to protect your personal data from unauthorized access, use, or disclosure.</p>
    
    <h2>Changes to This Privacy Policy</h2>
    <p>We may update this Privacy Policy from time to time. We will notify you of any changes by updating the "Effective Date" at the top of this page.</p>
    
    <h2>Contact Us</h2>
    <p>If you have questions or comments about this Privacy Policy, please contact us at: {contact_email}</p>
</body>
</html>
"""

def generate_privacy_policy(company_name, contact_email, output_file='privacy_policy.html'):
    effective_date = datetime.now().strftime("%B %d, %Y")
    privacy_policy = privacy_template.format(
        company_name=company_name,
        effective_date=effective_date,
        contact_email=contact_email
    )
    
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(privacy_policy)
    print(f"Privacy Policy saved as {output_file}")

# Example usage
generate_privacy_policy(
    company_name="GanjaGenius",
    contact_email="support@ganjagenius.com"
)