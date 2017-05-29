from flask_assets import Bundle

def create_assets(assets):
    # js = Bundle(
    #     'vendor/jquery/dist/jquery.min.js',
    #     output='js/libs.js'
    # )
    # assets.register('JS_FRAMEWORS', js)

    css = Bundle(
        'css/sticky-footer.css',
        output='css/min.css'
    )
    assets.register('CSS_FRAMEWORKS', css)