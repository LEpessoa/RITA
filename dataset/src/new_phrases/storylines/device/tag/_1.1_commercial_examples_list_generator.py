import time
import pyperclip
import _1_examples_list as _1
import undetected_chromedriver as uc 
from undetected_chromedriver import By
import time

# CSS selectors for the elements in the chatGPT web interface
next_button_selector = "#headlessui-dialog-panel-\:r1\: > div.prose.dark\:prose-invert > div.flex.gap-4.mt-6 > button > div"
next_button_selector2 = "#headlessui-dialog-panel-\:r1\: > div.prose.dark\:prose-invert > div.flex.gap-4.mt-6 > button.btn.relative.btn-neutral.ml-auto > div"
done_button_selector = "#headlessui-dialog-panel-\:r1\: > div.prose.dark\:prose-invert > div.flex.gap-4.mt-6 > button.btn.relative.btn-primary.ml-auto > div"
# textarea_selector = "#__next > div.overflow-hidden.w-full.h-full.relative > div.flex.h-full.flex-1.flex-col.md\:pl-\[260px\] > main > div.absolute.bottom-0.left-0.w-full.border-t.md\:border-t-0.dark\:border-white\/20.md\:border-transparent.md\:dark\:border-transparent.md\:bg-vert-light-gradient.bg-white.dark\:bg-gray-800.md\:\!bg-transparent.dark\:md\:bg-vert-dark-gradient > form > div > div.flex.flex-col.w-full.py-2.flex-grow.md\:py-3.md\:pl-4.relative.border.border-black\/10.bg-white.dark\:border-gray-900\/50.dark\:text-white.dark\:bg-gray-700.rounded-md.shadow-\[0_0_10px_rgba\(0\,0\,0\,0\.10\)\].dark\:shadow-\[0_0_15px_rgba\(0\,0\,0\,0\.10\)\] > textarea"
textarea_selector = "#__next > div.overflow-hidden.w-full.h-full.relative.flex > div > main > div.absolute.bottom-0.left-0.w-full.border-t.md\:border-t-0.dark\:border-white\/20.md\:border-transparent.md\:dark\:border-transparent.md\:bg-vert-light-gradient.bg-white.dark\:bg-gray-800.md\:\!bg-transparent.dark\:md\:bg-vert-dark-gradient.pt-2 > form > div > div.flex.flex-col.w-full.py-2.flex-grow.md\:py-3.md\:pl-4.relative.border.border-black\/10.bg-white.dark\:border-gray-900\/50.dark\:text-white.dark\:bg-gray-700.rounded-md.shadow-\[0_0_10px_rgba\(0\,0\,0\,0\.10\)\].dark\:shadow-\[0_0_15px_rgba\(0\,0\,0\,0\.10\)\] > textarea"
send_prompt_button_selector = "#__next > div.overflow-hidden.w-full.h-full.relative > div.flex.h-full.flex-1.flex-col.md\:pl-\[260px\] > main > div.absolute.bottom-0.left-0.w-full.border-t.md\:border-t-0.dark\:border-white\/20.md\:border-transparent.md\:dark\:border-transparent.md\:bg-vert-light-gradient.bg-white.dark\:bg-gray-800.md\:\!bg-transparent.dark\:md\:bg-vert-dark-gradient > form > div > div.flex.flex-col.w-full.py-2.flex-grow.md\:py-3.md\:pl-4.relative.border.border-black\/10.bg-white.dark\:border-gray-900\/50.dark\:text-white.dark\:bg-gray-700.rounded-md.shadow-\[0_0_10px_rgba\(0\,0\,0\,0\.10\)\].dark\:shadow-\[0_0_15px_rgba\(0\,0\,0\,0\.10\)\] > button"
copy_code_button_selector = "button.flex"
new_chat_button_selector = "#__next > div.overflow-hidden.w-full.h-full.relative > div.dark.hidden.bg-gray-900.md\:fixed.md\:inset-y-0.md\:flex.md\:w-\[260px\].md\:flex-col > div > div > nav > a.flex.py-3.px-3.items-center.gap-3.rounded-md.hover\:bg-gray-500\/10.transition-colors.duration-200.text-white.cursor-pointer.text-sm.mb-2.flex-shrink-0.border.border-white\/20"
bin_button_selector = "#__next > div.overflow-hidden.w-full.h-full.relative > div.dark.hidden.bg-gray-900.md\:fixed.md\:inset-y-0.md\:flex.md\:w-\[260px\].md\:flex-col > div > div > nav > div > div > a.flex.py-3.px-3.items-center.gap-3.relative.rounded-md.cursor-pointer.break-all.pr-14.bg-gray-800.hover\:bg-gray-800.group.animate-flash > div.absolute.flex.right-1.z-10.text-gray-300.visible > button:nth-child(2)"
confirm_bin_button_selector = "#__next > div.overflow-hidden.w-full.h-full.relative > div.dark.hidden.bg-gray-900.md\:fixed.md\:inset-y-0.md\:flex.md\:w-\[260px\].md\:flex-col > div > div > nav > div > div > a.flex.py-3.px-3.items-center.gap-3.relative.rounded-md.cursor-pointer.break-all.pr-14.bg-gray-800.hover\:bg-gray-800.group.animate-flash > div.absolute.flex.right-1.z-10.text-gray-300.visible > button:nth-child(1)"

options = uc.ChromeOptions()
# options.headless = True
driver = uc.Chrome(use_subprocess=True, options=options)
driver.get("https://chat.openai.com/auth/login") 
driver.maximize_window()
wait_on_input = input("Can I proceed?") # Wait for login preparations
full_list = _1.tag_examples
how_many_examples = 20
if __name__ == "__main__":
    total_length = len(_1.tag_examples)
    count = 0
    step = 2   
    while (count < total_length):   
        current_tag_list = full_list[count:count+step]
        print(20*"#")
        myPhrase = f"""Tags are a type of IoT Device.\\nHere is the definition of tag:\\nTags are labels or other physical objects used to identify the Physical Entity to which it is attached.Tags are used to identify Physical Entities, to which the Tags are usually physically attached. The identification process is called “reading”, and it is carried out by specific Sensor Devices, which are usually called readers. The primary purpose of Tags is to facilitate and increase the accuracy of the identification process. This process can be optical, as in the case of barcodes and QR codes, or it can be RF-based, as in the case of microwave car-plate recognition systems and RFID.\\n\\nHere is a list of tag examples:\\n```python\\ntag_examples = {current_tag_list}\\n```\\nFor each example in the tag_examples list, give me 10 commercially available examples of tags.
"""
        print(20*"#")
        print(myPhrase)
        print(20*"#")
        print(f"""Current item: {count+1}:{count+1+step} OF {len(full_list)}""")
        driver.find_element(By.CSS_SELECTOR,textarea_selector).send_keys(myPhrase)
        input("Continue?")
        count += step
        if count > total_length:
            count = total_length
    input("The list is over, press enter to close the browser.")