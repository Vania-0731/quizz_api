# 🧠 Quiz API

A RESTful API for managing quizzes, user attempts, profiles, and analytics using Django and Django REST Framework.

Repository: [https://github.com/Vania-0731/quizz_api.git](https://github.com/Vania-0731/quizz_api.git)

---

## 📦 Project Structure

This project is divided into the following Django apps:

- **quizzes**: Core logic for quizzes, questions, and answer choices.
- **categories**: Handles quiz categorization and tagging.
- **users**: Manages user profiles and their quiz attempts.
- **analytics**: Offers basic analytics like question stats and quiz activity.
- **config**: Main project configuration and routing.

---

## 🚀 Features

- 📋 Full CRUD for quizzes, categories, and user attempts.
- 👤 Profile system extending Django's User model with avatar & bio.
- 📈 Analytics endpoints to track quiz performance and user activity.
- 🔐 Authentication required for actions tied to specific users.
- 🌐 RESTful design with automatic browsable API via DRF.

---

## 🔌 API Endpoints

All endpoints are accessible under the `/api/` base path.

### Users

| Endpoint                       | Description                        |
|--------------------------------|------------------------------------|
| `/api/users/profiles/`        | Manage user profiles               |
| `/api/users/attempts/`        | Manage quiz attempts               |

### Quizzes

| Endpoint                      | Description                        |
|-------------------------------|------------------------------------|
| `/api/quizzes/`               | List, create, update quizzes       |
| `/api/questions/`             | Manage quiz questions              |
| `/api/choices/`               | Manage answer choices              |

### Categories

| Endpoint                      | Description                        |
|-------------------------------|------------------------------------|
| `/api/categories/`           | Manage quiz categories             |
| `/api/tags/`                 | Manage tags for quizzes            |

### Analytics

| Endpoint                               | Description                            |
|----------------------------------------|----------------------------------------|
| `/api/analytics/question-stats/`       | View statistics per question           |
| `/api/analytics/quiz-activities/`      | Track user quiz activity logs          |

### Auth

| Endpoint              | Description                        |
|-----------------------|------------------------------------|
| `/api-auth/login/`    | Login via DRF browsable API        |
| `/api-auth/logout/`   | Logout session                     |

---

## 🛠️ Local Setup

1. **Clone the repo**

```bash
git clone https://github.com/Vania-0731/quizz_api.git
cd quizz_api

