TechnoWiz Store - Django Starter (Windows + Razorpay)
========================================

Quick start (Windows)
---------------------
1. Install Python 3.10+ and create a virtualenv:
   python -m venv venv
   venv\Scripts\activate

2. Install requirements:
   pip install -r requirements.txt

3. Apply migrations and create superuser:
   python manage.py migrate
   python manage.py createsuperuser

4. Run server:
   python manage.py runserver

5. Admin:
   Visit http://127.0.0.1:8000/admin to add Products/Categories/LicenseKeys.
   Upload product files via the admin; they will be served in development from /media/.

Razorpay notes
--------------
- Replace RAZORPAY_KEY_ID and RAZORPAY_KEY_SECRET via environment variables or directly in techno_wiz/settings.py
- This starter uses a simple `razorpay_create_order` endpoint and client-side checkout. For production:
  * Verify payments server-side using Razorpay webhooks.
  * Use HTTPS and secure secrets.
  * Use storage like S3 for production file hosting and signed URLs for secure downloads.
