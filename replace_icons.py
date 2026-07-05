import os
import re

emoji_map = {
    '💻': '<i data-lucide="monitor"></i>',
    '📱': '<i data-lucide="smartphone"></i>',
    '☁️': '<i data-lucide="cloud"></i>',
    '🤖': '<i data-lucide="bot"></i>',
    '🔒': '<i data-lucide="shield"></i>',
    '📊': '<i data-lucide="bar-chart-3"></i>',
    '🎨': '<i data-lucide="palette"></i>',
    '🔗': '<i data-lucide="link"></i>',
    '📡': '<i data-lucide="radio"></i>',
    '🕶️': '<i data-lucide="glasses"></i>',
    '💼': '<i data-lucide="linkedin"></i>',
    '🐦': '<i data-lucide="twitter"></i>',
    '🐙': '<i data-lucide="github"></i>',
    '▶️': '<i data-lucide="youtube"></i>',
    '📍': '<i data-lucide="map-pin"></i>',
    '📞': '<i data-lucide="phone"></i>',
    '✉️': '<i data-lucide="mail"></i>',
    '🕐': '<i data-lucide="clock"></i>',
    '💡': '<i data-lucide="lightbulb"></i>',
    '🤝': '<i data-lucide="handshake"></i>',
    '⭐': '<i data-lucide="star"></i>',
    '🌱': '<i data-lucide="leaf"></i>',
    '🌍': '<i data-lucide="globe"></i>',
    '🏆': '<i data-lucide="award"></i>',
    '👥': '<i data-lucide="users"></i>',
    '♻️': '<i data-lucide="recycle"></i>',
    '⚡': '<i data-lucide="zap"></i>',
    '🎯': '<i data-lucide="target"></i>',
    '🔐': '<i data-lucide="lock"></i>',
    '🌐': '<i data-lucide="globe"></i>',
    '⚛️': '<i data-lucide="atom"></i>',
    '🟢': '<i data-lucide="circle"></i>',
    '🐍': '<i data-lucide="code"></i>',
    '🐳': '<i data-lucide="box"></i>',
    '🔥': '<i data-lucide="flame"></i>',
    '🗄️': '<i data-lucide="database"></i>',
    '👁️': '<i data-lucide="eye"></i>',
    '⚙️': '<i data-lucide="settings"></i>',
    '🏗️': '<i data-lucide="building"></i>',
    '🏛️': '<i data-lucide="landmark"></i>',
    '🛡️': '<i data-lucide="shield-check"></i>',
    '🖼️': '<i data-lucide="image"></i>',
    '⛓️': '<i data-lucide="link-2"></i>',
    '⚕️': '<i data-lucide="cross"></i>',
    '🖨️': '<i data-lucide="printer"></i>',
    '🛠️': '<i data-lucide="wrench"></i>',
    '🏢': '<i data-lucide="building-2"></i>',
    '📈': '<i data-lucide="trending-up"></i>',
    '🛒': '<i data-lucide="shopping-cart"></i>',
    '📋': '<i data-lucide="clipboard-list"></i>',
    '🎓': '<i data-lucide="graduation-cap"></i>',
    '⏱️': '<i data-lucide="timer"></i>',
    '🏋️': '<i data-lucide="dumbbell"></i>',
    '🗺️': '<i data-lucide="map"></i>'
}

def replace_emojis_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    for emoji, icon in emoji_map.items():
        content = content.replace(emoji, icon)
    
    if '<script src="https://unpkg.com/lucide@latest"></script>' not in content:
        content = content.replace('</body>', '<script src="https://unpkg.com/lucide@latest"></script>\n<script>\n  lucide.createIcons();\n</script>\n</body>')
        
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")

for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.html'):
            replace_emojis_in_file(os.path.join(root, file))
