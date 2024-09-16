from django.shortcuts import render, redirect
from .forms import CarWashForm, OwnerForm, ComplianceForm, LocationForm, JoiningForm

def register_car_wash(request):
    if request.method == 'POST':
        carwash_form = CarWashForm(request.POST)
        owner_form = OwnerForm(request.POST)
        compliance_form = ComplianceForm(request.POST)
        location_form = LocationForm(request.POST)
        joining_form = JoiningForm(request.POST)

        if (carwash_form.is_valid() and owner_form.is_valid() and 
            compliance_form.is_valid() and location_form.is_valid() and joining_form.is_valid()):
            
            # Save CarWash first to get CarWashID
            carwash = carwash_form.save()

            # Set CarWashID for other forms
            owner = owner_form.save(commit=False)
            owner.CarWashID = carwash
            owner.save()

             # Set CarWashID in the Compliance form and save it
            compliance = compliance_form.save(commit=False)
            compliance.CarWashID = carwash
            compliance.save()

             # Set CarWashID in the Location form and save it
            location = location_form.save(commit=False)
            location.CarWashID = carwash
            location.save()

            # Set CarWashID in the Joining form and save it
            joining = joining_form.save(commit=False)
            joining.CarWashID = carwash
            joining.save()

            # Redirect to a success page after saving all the forms
            return redirect('registration_success')

    else:
        # Instantiate empty forms if the request method is not POST (for rendering the form on GET request)
        carwash_form = CarWashForm()
        owner_form = OwnerForm()
        compliance_form = ComplianceForm()
        location_form = LocationForm()
        joining_form = JoiningForm()

        
    # Render the form page with all the forms
    return render(request, 'CarWashApp/CarWash.html', {
        'carwash_form': carwash_form,
        'owner_form': owner_form,
        'compliance_form': compliance_form,
        'location_form': location_form,
        'joining_form': joining_form
    })

def carwash_success(request):
    # Render the success page after successful registration
    return render(request, 'CarWashApp/success.html')


# Create your views here.
