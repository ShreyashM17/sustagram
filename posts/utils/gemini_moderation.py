# posts/utils/gemini_moderation.py

import mimetypes
from django.conf import settings
import google.generativeai as genai

def is_image_sustainable(image_path, caption=""):
    """
    Uses Google Gemini to check if an image (optionally + caption) is sustainability related.
    Returns True if AI thinks image fits our sustainability criteria.
    """
    # ✅ Bypass moderation if disabled
    if not settings.ENABLE_GEMINI_MODERATION:
        return True

    # ✅ Initialize Gemini
    genai.configure(api_key=settings.GEMINI_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')

    # ✅ Detect image MIME type
    mime_type, _ = mimetypes.guess_type(image_path)
    if not mime_type:
        mime_type = "image/jpeg"  # fallback

    with open(image_path, "rb") as img_file:
        image_data = img_file.read()

    # ✅ Build prompt for higher accuracy
    prompt = (
        "You are an expert environmental assistant. "
        "Please analyze the attached image and optional user caption. "
        "Determine if the image shows any eco-friendly, sustainability, nature, recycling, "
        "tree planting, gardening, composting, or environmental conservation activity. "
        "Only reply with exactly YES if it does, or NO if it does not."
    )

    # ✅ Multimodal input: text + image + caption
    contents = [
        {"text": prompt},
        {"inline_data": {"mime_type": mime_type, "data": image_data}},
        {"text": f"User caption: {caption}"}
    ]

    # ✅ Call Gemini
    response = model.generate_content(contents)

    result_text = response.text.strip().lower()
    print(f"[Gemini] Moderation result: {result_text}")  # You can remove this line later

    return "yes" in result_text
