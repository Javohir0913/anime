from django.http import HttpRequest
from user_agents import parse

def get_device_info(request: HttpRequest):
    user_agent_str = request.META.get("HTTP_USER_AGENT", "")
    user_agent = parse(user_agent_str)

    if user_agent.is_mobile:
        device_type = "Telefon"
        brand = user_agent.device.brand or "Noma'lum"
        model = user_agent.device.model or "Noma'lum"
    elif user_agent.is_tablet:
        device_type = "Planshet"
        brand = user_agent.device.brand or "Noma'lum"
        model = user_agent.device.model or "Noma'lum"
    elif user_agent.is_pc:
        device_type = "Kompyuter"
        brand = user_agent.os.family  # Windows, macOS, Linux
        model = user_agent.browser.family  # Chrome, Firefox, Edge
    else:
        device_type = "Noma'lum qurilma"
        brand = "Noma'lum"
        model = "Noma'lum"

    return {
        "device_type": device_type,
        "brand": brand,
        "model": model
    }
