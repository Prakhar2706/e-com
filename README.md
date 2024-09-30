# E-com

E-com is a simple Django-based e-commerce website that links to Amazon and Flipkart to display products. The website provides a user-friendly experience with essential features like user login, registration, contact forms, and a responsive design.

![image](https://github.com/user-attachments/assets/49dd76e5-d0ef-4ab4-94c1-63dbcc3d155e)
![image](https://github.com/user-attachments/assets/c8062a87-2734-4a91-8bc5-6ba6d2fde3a9)
![image](https://github.com/user-attachments/assets/2535cae9-049f-41d6-8bc1-47daf646b6f8)
![image](https://github.com/user-attachments/assets/1a86be48-4f62-4be7-ab5e-4c8988c59147)
![image](https://github.com/user-attachments/assets/1e14d770-57f5-47bb-b458-04e3f66ad298)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Prakhar2706/e-com.git
   ```
2. Navigate to the project directory:
   
   ```bash
   cd e-com
   ```
3. Create a virtual environment:
   
   ```bash
   python -m venv env
   ```
4. Activate the virtual environment:

   * On Windows:
     
   ```bash
   .\env\Scripts\activate
   ```

   *On macOS/Linux:
   
   ```bash
   source env/bin/activate
   ```
5. Install the dependencies:
   
   ```bash
   pip install -r requirements.txt
   ```
6. Create migrations for your models:

   ```bash
   python manage.py makemigrations
   ```
7. Apply migrations:
   
   ```bash
   python manage.py migrate
   ```
8. Create a superuser:

   ```bash
   python manage.py createsuperuser
   ```
9. Start the development server:
   
   ```bash
   python manage.py runserver
   ```
10. Visit http://127.0.0.1:8000 in your browser to access the app.

11. For admin panel:
    
    ```bash
    http://127.0.0.1:8000/admin
    ```

## Features

- **User Login**: Users can securely log in to access their accounts.
- **User Registration**: New users can create an account easily.
- **Contact Form**: Users can reach out via a simple contact form.
- **About Section**: Includes an "About" page with details about the site.
- **User Friendly**: Simple and easy-to-navigate interface.
- **Responsive Design**: Works well on all screen sizes, including mobile devices.
- **Product Links**: Shows products from Amazon and Flipkart.

## Requirements

Django==5.0.7

## Usage

- User Login & Registration: Users can sign up and log in to access additional features.
- Product Display: The site displays products from Amazon and Flipkart.
- Contact Form: Users can submit inquiries through the contact form.
- Responsive UI: The design adjusts smoothly across devices for an optimal user experience.
