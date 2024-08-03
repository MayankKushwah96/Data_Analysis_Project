import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from django.shortcuts import render
from .forms import UploadFileForm
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():

            file = request.FILES['file']
            fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'uploads'))
            filename = fs.save(file.name, file)
            file_path = fs.path(filename)

            data = pd.read_csv(file_path)
            summary_stats = data.describe().to_html(classes='table table-striped')
            missing_values = data.isnull().sum().to_frame('Missing Values').to_html(classes='table table-striped')

         
            hist_dir = os.path.join(settings.MEDIA_ROOT, 'histograms')
            os.makedirs(hist_dir, exist_ok=True)

         
            histograms = []
            for column in data.select_dtypes(include=[float, int]).columns:
                plt.figure(figsize=(14, 8))
                sns.set(style="whitegrid")
                
                
                palette = sns.color_palette("Blues", n_colors=10)
                
                # Plot histogram
                ax = sns.histplot(
                    data[column].dropna(), 
                    bins=20,  
                    kde=False, 
                    color='royalblue', 
                    edgecolor='black'
                )
                
               
                plt.title(f'Distribution of {column.replace("_", " ").title()}', fontsize=18)
                plt.xlabel(column.replace("_", " ").title(), fontsize=16)
                plt.ylabel('Frequency', fontsize=16)
                
               
                for p in ax.patches:
                    width = p.get_width()
                    height = p.get_height()
                    x = p.get_x() + width / 2
                    y = p.get_y() + height
                    ax.annotate(f'{int(height)}', (x, y), ha='center', va='bottom', fontsize=12, color='black')

                
                plt.grid(True, linestyle='--', alpha=0.7)
              
                hist_filename = f'histogram_{column}.png'
                hist_path = os.path.join(hist_dir, hist_filename)
                plt.savefig(hist_path, bbox_inches='tight', dpi=300)
                plt.close()
                
                histograms.append({
                    'url': os.path.join(settings.MEDIA_URL, 'histograms', hist_filename),
                    'title': column.replace('_', ' ').title()
                })

            context = {
                'summary_stats': summary_stats,
                'missing_values': missing_values,
                'histograms': histograms,
            }

            return render(request, 'analysis/results.html', context)
    else:
        form = UploadFileForm()
    return render(request, 'analysis/upload.html', {'form': form})
