from django.shortcuts import render
from django.core.mail import send_mail
from django.http import JsonResponse
from .forms import ContactForm

# Create your views here.
def home(request):
    return render(request, 'index.html')



def ContactFormView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Send the email
            try:
                send_mail(
                    subject=f"New Contact Form Submission: {subject}",
                    message=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}",
                    from_email=email,
                    recipient_list=['youremail@example.com'],  # Replace with your email
                    fail_silently=False,
                )
                return JsonResponse({'message': 'Your message has been sent successfully.'})
            except Exception as e:
                return JsonResponse({'error': 'Failed to send email. Try again later.'}, status=500)
        else:
            return JsonResponse({'error': 'Invalid form data.'}, status=400)

    form = ContactForm()
    return render(request, 'contact.html', {'form': form})


