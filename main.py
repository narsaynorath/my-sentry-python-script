import sentry_sdk
sentry_sdk.init(
    "http://94c8b3009e974f60b88b1dded4f71546@dev.getsentry.net:8000/2",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)

division_by_zero = 1 / 0
