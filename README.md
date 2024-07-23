# Library App

This is a Single Page Application (SPA) for managing a library's books and readers. The application allows users to browse books, check out and return books, and manage reader details.

## Features

- **Book List**: Browse a collection of books with details like title, author, and availability.
- **Book Details**: View detailed information about each book, including its status, readers who have taken it out, and options to check out or request the book.
- **Reader List**: View a list of readers, the books they have taken out, and navigate to their detailed profiles.
- **Reader Details**: View detailed information about each reader, including the books they have taken out.

## Technologies Used

- **Frontend**: Vue.js for building a reactive and dynamic user interface.
- **Backend**: Django for creating a robust and scalable API.
- **Styling**: Tailwind CSS for a clean and responsive design.

## Project Structure

- **frontend/src/components/BookList.vue**: Displays a list of books with basic information and availability status.
- **frontend/src/components/BookDetails.vue**: Shows detailed information about a specific book, allows for checking out, unchecking out, and requesting the book.
- **frontend/src/components/ReaderList.vue**: Displays a list of readers and the books they have taken out.
- **frontend/src/components/ReaderDetails.vue**: Shows detailed information about a specific reader and their borrowed books.
- **backend**: Contains the Django backend that provides the API for the frontend.

## Installation

### Clone the repository

1. **Clone the repository**:
    ```sh
    git clone https://github.com/your-username/library-app.git
    cd library-app
    ```

### Backend

1. **Navigate to the backend directory**:
    ```sh
    cd backend
    ```

2. **Install dependencies**:
    Make sure you have Python installed, then use pip to install the required packages. You might need to manually install Django and any other dependencies:
    ```sh
    pip install django djangorestframework
    ```

3. **Run migrations**:
    ```sh
    python manage.py migrate
    ```

4. **Run the development server**:
    ```sh
    python manage.py runserver
    ```

### Frontend

1. **Navigate to the frontend directory**:
    ```sh
    cd ../frontend
    ```

2. **Install dependencies**:
    Make sure you have Node.js and npm installed, then run:
    ```sh
    npm install
    ```

3. **Run the application**:
    ```sh
    npm run serve
    ```

## Usage

### Viewing Books

1. **Book List**:
   - Navigate to the home page to view a list of books.
   - Click on a book title to view its details.

2. **Book Details**:
   - View detailed information about the book.
   - Check out the book if it's available by selecting a reader and clicking the "Check Out" button.
   - If the book is checked out, uncheck it by clicking the "Uncheck Out" button.

### Managing Readers

1. **Reader List**:
   - Navigate to the readers page to view a list of readers.
   - Click on a reader's name to view their details.

2. **Reader Details**:
   - View detailed information about the reader.
   - See the list of books they have taken out.

## API Endpoints

- **Books**:
  - `GET /api/books/`: Fetch a list of books.
  - `GET /api/books/:id/`: Fetch details of a specific book.
  - `POST /api/books/:id/checkout/`: Check out a book.
  - `POST /api/books/:id/uncheckout/`: Uncheck out a book.
  - `POST /api/books/:id/request/`: Request a book.

- **Readers**:
  - `GET /api/readers/`: Fetch a list of readers.
  - `GET /api/readers/:id/`: Fetch details of a specific reader.

