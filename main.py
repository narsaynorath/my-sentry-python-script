import sentry_sdk
sentry_sdk.init(
    "https://63b144e42c8145439b12b8104c5fb87a@o1052590.ingest.sentry.io/6036739",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)

division_by_zero = 1 / 0
