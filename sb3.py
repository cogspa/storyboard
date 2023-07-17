import csv

# Define the HTML template
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Card Layout Example</title>
  <style>
    .main {{
      width: 1920px;
      height: 1080px;
      border: 1px solid #000;
    }}

    .container {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      grid-gap: 10px;
    }}

    .card {{
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      border: 1px solid #000;
      height: 500px;
    }}

    .frame {{
      width: 540px;
      height: 300px;
      border: 1px solid #000;
    }}

    .caption {{
      text-align: center;
    }}
  </style>
</head>
<body>
  {main_divs}
</body>
</html>
"""

main_div_template = """
<div class="main">
  <div class="container">
    {cards}
  </div>
</div>
"""

card_template = """
<div class="card">
  <div class="frame"></div>
  <div class="caption">
    <h5>Panel: {panel} Camera Angle: {camera_angle} Caption: {caption} Narration: {narration} Timing: {timing}</h5>
  </div>
</div>
"""

# Read the CSV file
with open('data.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    cards = [card_template.format(panel=row['Panel'], 
                                  camera_angle=row['Camera Angle'], 
                                  caption=row['Caption'], 
                                  narration=row['Narration'], 
                                  timing=row['Timing']) for row in reader]

# Group cards into chunks of 6
grouped_cards = [cards[i:i+6] for i in range(0, len(cards), 6)]
# Create main divs for each group
main_divs = [main_div_template.format(cards="\n".join(group)) for group in grouped_cards]

# Combine the main divs into a single string
main_divs_html = "\n".join(main_divs)

# Insert the main divs into the HTML template and write it to a file
html = html_template.format(main_divs=main_divs_html)
with open('index2.html', 'w') as f:
    f.write(html)
