# CSV Data Analysis Web Application

## Description

This project is a Django-based web application that allows users to upload CSV files, perform basic data analysis, and display the results and plots. The application uses Django for web functionality, pandas for data analysis, and matplotlib or seaborn for data visualization.

### Features

- **CSV File Upload**: Users can upload CSV files through a web form.
- **Temporary Storage**: Uploaded files are stored temporarily for processing.
- **Data Analysis**: 
  - Display the first few rows of the data.
  - Calculate summary statistics such as mean, median, and standard deviation for numerical columns.
  - Identify and handle missing values.
- **Data Visualization**: 
  - Generate histograms for numerical columns.
  - Display plots on the web page using matplotlib or seaborn.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/MayankKushwah96/Data_Analysis_Project.git
    ```

2. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply the database migrations:
    ```bash
    python manage.py migrate
    ```

5. Create a superuser for accessing the Django admin panel: (optional)
    ```bash
    python manage.py createsuperuser
    ```

## Running the Application

1. Make sure you're in the project directory and the virtual environment is activated.
2. Run the Django development server:
    ```bash
    python manage.py runserver
    ```

3. Open a web browser and go to `http://127.0.0.1:8000` to access the application.

## Usage

1. **Upload CSV File**: Navigate to the upload page and choose a CSV file to upload. The file will be processed and analyzed.
2. **View Results**: After uploading, the application will display:
    - The first few rows of the data.
    - Summary statistics for numerical columns.
    - Information about missing values.
    - Histograms for numerical columns.

## Project Structure

- `myproject/`: Root directory of the Django project.
- `analysis/`: Django app handling the CSV upload and data analysis.
  - `views.py`: Contains views for handling file uploads and displaying results.
  - `models.py`: Defines models for storing uploaded files.
  - `forms.py`: Contains the form for file uploads.
  - `urls.py`: URL routing for the analysis app.
  - `templates/analysis/`: HTML templates for the analysis views.
- `requirements.txt`: File listing the project's dependencies.

## Dependencies

- Python
- Django
- pandas
- matplotlib or seaborn
- Other dependencies listed in `requirements.txt`


