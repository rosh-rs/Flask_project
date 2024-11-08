from flask import Flask,request,render_template
import random
import string

app = Flask(__name__)



@app.route('/')
def main():
    return render_template('page.html')

@app.route('/home')
@app.route('/home/')
def home():
    return render_template('home.html')

@app.route('/genpassword', methods=['GET', 'POST'])
def genpassword():
    min_length = 8
    max_length = 25

    passlen = int(request.form.get('passlen'))

    if passlen < min_length:
        wrong = f" At least create a {min_length} digit password..."
        return render_template('home.html', m=wrong)

    if passlen > max_length:
        wrong =f" Can create a max {max_length} digit password..."
        return render_template('home.html', m=wrong)

    include_numbers = request.form.get('numbers')
    include_special_chars = request.form.get('splchar')
    include_uppercase_letters = request.form.get('uppercase')

    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_chars = '%@#&'

    char_sets = [lowercase_letters]

    if include_numbers == 'on':
        char_sets.append(digits)
    if include_special_chars == 'on':
        char_sets.append(special_chars)
    if include_uppercase_letters == 'on':
        char_sets.append(uppercase_letters)

    password_chars = []
    if include_special_chars == 'on':
        password_chars.append(random.choice(special_chars))  

    all_chars = ''.join(char_sets)
    
    remaining_length = passlen - len(password_chars)

    if remaining_length > 0:
        password_chars += random.choices(all_chars, k=remaining_length)

    random.shuffle(password_chars)

    password = ''.join(password_chars)

    return render_template('pass.html', generatedpassword=password)

if __name__ == '__main__':
    app.run(debug=True)