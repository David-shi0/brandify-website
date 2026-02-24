from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm

class HomeView(TemplateView):
    template_name = 'core/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Brandify - Building Brands That Connect & Grow'
        return context

class AboutView(TemplateView):
    template_name = 'core/about.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'About Us - Brandify'
        return context

class ServicesView(TemplateView):
    template_name = 'core/services.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Our Services - Brandify'
        return context

class TeamView(TemplateView):
    template_name = 'core/team.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Our Team - Brandify'
        context['team_members'] = [
            {'name': 'Erick Paul', 'role': 'Founder & CEO', 'bio': 'Visionary leader with passion for digital innovation'},
            {'name': 'Ernest Mbwana', 'role': 'Creative Director', 'bio': 'Award-winning designer and brand strategist'},
            {'name': 'Steve Semhomba', 'role': 'Marketing Head', 'bio': 'Digital marketing expert with 8+ years experience'},
            {'name': 'Lucy Mgaya', 'role': 'Content Strategist', 'bio': 'Storytelling specialist creating brand narratives'},
        ]
        return context

class ContactView(TemplateView):
    template_name = 'core/contact.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Contact Us - Brandify'
        context['contact_info'] = {
            'phone': '+255 742 076 974',
            'email': 'shiodavid41@gmail.com',
            'address': 'Machava Kigamboni, Dar es salaam',
            'registration': '614618'
        }
        context['form'] = ContactForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            # Get form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            
            # Send email (configure email settings first)
            try:
                send_mail(
                    f'New Contact from {name} - Brandify Website',
                    f'Name: {name}\nEmail: {email}\nPhone: {phone}\n\nMessage:\n{message}',
                    email,  # From email
                    ['shiodavid41@gmail.com'],  # To email
                    fail_silently=False,
                )
                messages.success(request, 'Thank you for contacting us! We\'ll get back to you soon.')
            except:
                messages.error(request, 'Sorry, there was an error sending your message. Please try again.')
            
            return redirect('contact')
        
        # If form is invalid
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return render(request, self.template_name, context)