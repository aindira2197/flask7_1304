from flask import Flask, render_template

app = Flask(__name__)

ranglar = ["Qizil", "Yashil", "Ko'k", "Sariq", "To'q sariq", "Binafsha"]

@app.route('/ranglar/<rang>/info')
def rang_info(rang):
    rang_lower = rang.lower()

    for i, r in enumerate(ranglar):
        if r.lower() == rang_lower:
            return render_template(
                'rang_info.html',
                topildi=True,
                rang=r,
                uzunlik=len(r),
                indeks=i
            )
    return render_template(
        'rang_info.html',
        topildi=False,
        ranglar=ranglar
    )

if __name__ == "__main__":
    app.run(debug=True)
