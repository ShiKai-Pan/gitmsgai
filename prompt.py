def get_prompt(language: str="en") -> str:
    """
    Generate a prompt for the AI model.
    """
    return (
        f"請幫我依據我給的 git diff，幫我擬定commit message({language})，包含message title與條列的 message body\n"
        "並且進行 feat、refactor之類的分類與描述\n"
        "其中的敘述盡可能的簡潔明瞭\n"
        f"同時 git message與 body 請用{language}\n"
        "並且保留原先的專有名詞、元件名稱不要翻譯，例如：Asset，請不要翻譯，以此類推⋯\n"
        "最後 git 以外的補充說明的部分請用正體中文與台灣習慣用語\n"
        "下面是一個範例：\n"
        "refactor(ui): Enhance home page and punch functionality\n\n"
        "- Update logo assets and add small logo variant\n"
        "- Improve HomeBody layout with dividers and consistent styling\n"
        "- Refine PunchPage UI with better spacing and typography\n"
        "- Enhance NuetCheckList appearance and behavior\n"
        "- Update translations and icon usage"
    )