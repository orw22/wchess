class AppConstants:
    DECISECONDS_PER_MINUTE = 600


class RateLimitConfig:
    CONCURRENT_GAME_LIMIT = 100
    BUCKET_CAPACITY = 100
    INITIAL_TOKENS = 20
    REFILL_RATE_MINUTE = 4
