from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Bank
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Route for creating a bank
@app.route('/bank/create', methods=['GET', 'POST'])
def create_bank():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        location = request.form.get('location', '').strip()
        if not name or not location or len(name) > 50 or len(location) > 100:
            # Input validation failed
            return render_template('create_bank.html', error="Invalid input.")
        bank = Bank(name=name, location=location)
        try:
            db.session.add(bank)
            db.session.commit()
        except Exception as e:
            # Handle database error
            db.session.rollback()
            return render_template('create_bank.html', error="Database error.")
        return redirect(url_for('list_banks'))
    return render_template('create_bank.html')

# Route for listing all banks
@app.route('/banks')
def list_banks():
    banks = Bank.query.all()
    return render_template('list_banks.html', banks=banks)

# Route for displaying details of a specific bank
@app.route('/bank/<int:bank_id>')
def view_bank(bank_id):
    bank = Bank.query.get_or_404(bank_id)
    return render_template('view_bank.html', bank=bank)

@app.route('/')
def home():
    return render_template('home.html')

#deleting banks
@app.route('/delete_bank', methods=['GET', 'POST'])
def delete_bank():
    if request.method == 'POST':
        bank_id = request.form['bank_id']
        bank = Bank.query.get_or_404(bank_id)
        bank_name = bank.name
        db.session.delete(bank)
        db.session.commit()

        banks = Bank.query.all()
        remaining_banks = [bank.name for bank in banks]
        success_message = f"Bank '{bank_name}' deleted successfully. Your remaining banks: {', '.join(remaining_banks)}"
        return render_template('list_banks.html', message=success_message, banks=banks)
    else:
        banks = Bank.query.all()
        return render_template('delete_bank.html', banks=banks)

   
@app.route('/bank/update', methods=['GET', 'POST'])
def update_bank():
    if request.method == 'POST':
        bank_id = request.form['bank_id']
        name = request.form['name'].strip()
        location = request.form['location'].strip()

        # Input validation
        if not name or not location or len(name) > 50 or len(location) > 100:
            # Invalid input, render the form again with an error message
            banks = Bank.query.all()
            return render_template('update_bank.html', banks=banks, error="Invalid input.")

        bank = Bank.query.get(bank_id)

        if bank is None:
            # No bank with the given id exists
            return render_template('update_bank.html', error="No such bank exists.")

        try:
            bank.name = name
            bank.location = location
            db.session.commit()
        except Exception as e:
            # Handle database error
            db.session.rollback()
            banks = Bank.query.all()
            return render_template('update_bank.html', banks=banks, error="Database error.")
        
        return redirect(url_for('view_bank', bank_id=bank_id))

    banks = Bank.query.all() # get all banks
    return render_template('update_bank.html', banks=banks, error="Invalid input.")

