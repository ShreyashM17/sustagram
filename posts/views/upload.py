from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from posts.forms import PostForm
from django.contrib import messages
from django.utils import timezone
from posts.utils.gemini_moderation import is_image_sustainable

GREEN_SCORE_PER_POST = 10

@login_required
def upload_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()  # Save to get image file path

            image_path = post.image.path
            caption = post.caption or ""

            try:
                # 🔍 Run Gemini AI moderation check
                if not is_image_sustainable(image_path, caption):
                    post.delete()  # Rollback the post
                    messages.error(request, "❌ Upload rejected: This image does not appear to be sustainability related.")
                    return redirect('upload_post')
            except Exception as e:
                post.delete()  # Clean up post if error happens
                messages.error(request, f"❌ AI moderation failed: {str(e)}")
                return redirect('upload_post')

            # ✅ Passed moderation → update user green score
            request.user.green_score += GREEN_SCORE_PER_POST
            request.user.last_post_at = timezone.now()
            request.user.save(update_fields=["green_score", "last_post_at"])

            messages.success(request, f"✅ Post shared! 🌱 Your green score increased by {GREEN_SCORE_PER_POST}!")
            return redirect('feed')
    else:
        form = PostForm()

    return render(request, 'posts/upload.html', {'form': form})