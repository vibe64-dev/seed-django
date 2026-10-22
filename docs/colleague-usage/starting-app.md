# Start from the Django Basic app

When adding a project, choose **Django · Basic app** and **Use this starter**.
This works on desktop and phone. Successful import adds the application source
and its complete Genesis contracts to the session; use **Save** to keep that
work in the project.

Setup then creates the Python virtual environment, installs the pinned
requirements, creates an untracked development secret key and applies the
database migrations. Preview starts Django's development server and opens the
notes page. Saving a note proves the form, CSRF protection and database work.

The app has no visitor accounts. To use `/admin/`, ask the coding agent to
create a staff user for you; the starter ships none and never commits
passwords.

If import reports missing Stack contracts while the destination project is
still empty, the rejected starter needs repair. Once the starter is corrected,
retry **Use this starter**. Do not add placeholder Stack sections to the
destination merely to suppress the error.

Colleague can explain the choices and offer to apply the selected starter.
Only after your direct request or accepted offer may it apply that exact
configured starter through its existing onboarding action, then recheck the
result.
