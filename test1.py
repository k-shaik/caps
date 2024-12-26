import random
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import Dict
import pandas as pd
from sklearn.cluster import KMeans
from fpdf import FPDF
from geopy.geocoders import Nominatim
class AdvancedSecuritySimulator:
    def __init__(self,
                 gmail_email: str,
                 gmail_password: str,
                 recipient_email: str,
                 gemini_api_key: str = None):
        self.THREAT_TYPES = {
            "Phishing Attack": "High",
            "DDoS Attack": "High",
            "Malware Infection": "Medium",
            "Data Breach": "Critical",
            "SQL Injection": "Critical",
            "Ransomware Attack": "Critical",
            "Man-in-the-Middle": "High",
            "Zero-Day Exploit": "Critical",
            "Brute Force Attack": "Medium",
            "Cross-Site Scripting": "High"
        }

        self.ATTACK_SOURCES = {
            "North America": ["US", "CA"],
            "Europe": ["GB", "DE", "FR", "RU"],
            "Asia": ["CN", "JP", "KR", "IN"],
            "Other": ["BR", "AU"]
        }

        self.gmail_email = gmail_email
        self.gmail_password = gmail_password
        self.recipient_email = recipient_email
        self.incidents = []
        self.ml_model = self._initialize_ml_model()

        self.geolocator = Nominatim(user_agent="security_simulator")

    def _initialize_ml_model(self):
        model = KMeans(n_clusters=3, random_state=42)
        return model

        def send_security_alert(self, incident: Dict):
            try:
                msg = MIMEMultipart('alternative')
                msg['Subject'] = f"🚨 SECURITY ALERT: {incident['type']} Detected"
                msg['From'] = self.gmail_email
                msg['To'] = self.recipient_email

                # Define severity colors
                severity_colors = {
                    'Critical': '#ff0000',
                    'High': '#ff4500',
                    'Medium': '#ffa500',
                    'Low': '#ffff00'
                }
                severity_color = severity_colors.get(incident['severity'], '#ffffff')

                # Plain text version
                text = f"""
                  ⚠️ SECURITY INCIDENT DETECTED ⚠️

                  Incident ID: {incident['id']}
                  Time: {incident['time']}
                  Attack Type: {incident['type']}
                  Severity: {incident['severity']}
                  Region: {incident['region']}
                  Country: {incident['country']}

                  Recommended Response:
                  {incident.get('ai_response_plan', 'No specific response plan')}
                  """

                # HTML version with hacker theme
                html = f"""
                  <html>
                  <head>
                      <style>
                          body {{{{
                              background-color: #0a0a0a;
                              color: #00ff00;
                              font-family: 'Courier New', monospace;
                              padding: 20px;
                              line-height: 1.6;
                          }}}}
                          .container {{{{
                              border: 1px solid #00ff00;
                              padding: 20px;
                              max-width: 600px;
                              margin: 0 auto;
                              box-shadow: 0 0 10px #00ff00;
                          }}}}
                          .header {{{{
                              text-align: center;
                              border-bottom: 2px solid #00ff00;
                              padding-bottom: 10px;
                              margin-bottom: 20px;
                          }}}}
                          .warning-icon {{{{
                              font-size: 48px;
                              margin-bottom: 10px;
                          }}}}
                          .incident-details {{{{
                              background-color: #0f0f0f;
                              padding: 15px;
                              border-left: 3px solid #ff0000;
                              margin: 10px 0;
                          }}}}
                          .severity {{{{
                              display: inline-block;
                              padding: 5px 10px;
                              border-radius: 3px;
                              font-weight: bold;
                              margin: 5px 0;
                              background-color: {severity_color};
                              color: #000000;
                          }}}}
                          .blink {{{{
                              animation: blink 1s step-end infinite;
                          }}}}
                          @keyframes blink {{{{
                              50% {{{{
                                  opacity: 0;
                              }}}}
                          }}}}
                          .matrix-bg {{{{
                              background: linear-gradient(rgba(0, 255, 0, 0.05), rgba(0, 255, 0, 0.05));
                              padding: 20px;
                          }}}}
                          .response-plan {{{{
                              border: 1px dashed #00ff00;
                              padding: 15px;
                              margin-top: 20px;
                          }}}}
                          .timestamp {{{{
                              color: #888888;
                              font-size: 0.9em;
                          }}}}
                      </style>
                  </head>
                  <body>
                      <div class="container matrix-bg">
                          <div class="header">
                              <div class="warning-icon">⚠️</div>
                              <h1 class="blink">SECURITY ALERT</h1>
                              <div class="timestamp">{incident['time']}</div>
                          </div>

                          <div class="incident-details">
                              <h2>Incident #{incident['id']}</h2>
                              <p><strong>Attack Type:</strong> {incident['type']}</p>
                              <p><strong>Severity:</strong> <span class="severity">{incident['severity']}</span></p>
                              <p><strong>Location:</strong> {incident['region']} ({incident['country']})</p>
                              <p><strong>Coordinates:</strong> LAT: {incident['location']['lat']:.2f} LON: {incident['location']['lon']:.2f}</p>
                          </div>

                          <div class="response-plan">
                              <h3>→ Recommended Response Plan</h3>
                              <p>{incident.get('ai_response_plan', 'No specific response plan')}</p>
                          </div>

                          <div style="text-align: center; margin-top: 20px; font-size: 0.8em;">
                              <p>This is an automated security alert. Please respond according to security protocols.</p>
                              <p>Generated by Advanced Security Monitoring System</p>
                          </div>
                      </div>
                  </body>
                  </html>
                  """

            part1 = MIMEText(text, 'plain')
            part2 = MIMEText(html, 'html')

            msg.attach(part1)
            msg.attach(part2)

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
                server.login(self.gmail_email, self.gmail_password)
                server.sendmail(self.gmail_email, self.recipient_email, msg.as_string())
                print(f"Alert sent for incident {incident['id']}")

        except Exception as e:
            print(f"Failed to send email alert: {e}")

    def simulate_attack(self):
        attack_type = random.choice(list(self.THREAT_TYPES.keys()))
        severity = self.THREAT_TYPES[attack_type]
        region = random.choice(list(self.ATTACK_SOURCES.keys()))
        country = random.choice(self.ATTACK_SOURCES[region])
        location = self._get_country_coordinates(country)

        incident = {
            "id": len(self.incidents) + 1,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "type": attack_type,
            "severity": severity,
            "location": location,
            "region": region,
            "country": country,
            "ai_response_plan": "Activate Incident Response Plan."
        }

        self.incidents.append(incident)
        self.send_security_alert(incident)
        return incident

    def _get_country_coordinates(self, country_code: str) -> Dict:
        try:
            location = self.geolocator.geocode(country_code)
            return {'lat': location.latitude, 'lon': location.longitude}
        except:
            return {'lat': 0, 'lon': 0}

    def generate_pdf_report(self, filename: str = "security_report.pdf"):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", "B", 16)
        pdf.cell(0, 10, "Security Incident Report", ln=True, align="C")
        pdf.set_font("Arial", "", 10)

        stats = self.get_summary_statistics()
        for key, value in stats.items():
            pdf.cell(0, 8, f"{key}: {value}", ln=True)

        pdf.add_page()
        for incident in self.incidents[-5:]:
            pdf.set_font("Arial", "B", 10)
            pdf.cell(0, 8, f"Incident #{incident['id']}", ln=True)
            pdf.set_font("Arial", "", 10)
            pdf.cell(0, 6, f"Type: {incident['type']}", ln=True)
            pdf.cell(0, 6, f"Severity: {incident['severity']}", ln=True)
            pdf.cell(0, 6, f"Time: {incident['time']}", ln=True)
            pdf.cell(0, 6, "", ln=True)

        pdf.output(filename)

    def get_summary_statistics(self) -> Dict:
        if not self.incidents:
            return {}

        df = pd.DataFrame(self.incidents)
        return {
            "Total Incidents": len(self.incidents),
            "Most Common Attack": df['type'].mode()[0],
            "Average Severity": df['severity'].map({
                "Low": 1, "Medium": 2, "High": 3, "Critical": 4
            }).mean(),
            "Critical Incidents": len(df[df['severity'] == "Critical"]),
            "Last 24h Incidents": len(df[
                                          pd.to_datetime(df['time']) > pd.Timestamp.now() - pd.Timedelta(days=1)
                                          ])
        }


def main():
    simulator = AdvancedSecuritySimulator(
        gmail_email="khajashaikkanna@gmail.com",
        gmail_password="iqnk fmaa ucdb waxa",
        recipient_email="2200090018csit@gmail.com",
        gemini_api_key="AIzaSyCBwlkT9LJ2YJeuggiA_ohmkbAAtEIWiq0"

    )


    for _ in range(3):
        simulator.simulate_attack()

    simulator.generate_pdf_report()


if __name__ == "__main__":
    main()
