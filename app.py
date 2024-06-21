from flask import Flask, request, render_template_string

app = Flask(__name__)

# صفحة HTML تحتوي على النموذج
html_form = '''
<!doctype html>
<html>
<body>
    <form action="/submit" method="post">
        Email: <input type="text" name="email"><br>
        Password: <input type="password" name="password"><br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
'''

@app.route('/')
def form():
    return render_template_string(html_form)

@app.route('/submit', methods=['POST'])
def submit():
    email = request.form['email']
    password = request.form['password']
    
    # حفظ البيانات في ملف
    with open('user_data.txt', 'a') as f:
        f.write(f'Email: {email}, Password: {password}\n')
    
    return 'Data saved successfully!'

if __name__ == '__main__':
    app.run(debug=True)
