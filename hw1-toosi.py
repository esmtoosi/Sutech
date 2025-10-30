from scipy.stats import binom

# سوال 1: Circuit Switching
def max_users_circuit_switching(link_capacity=200, user_bandwidth=20):
    return link_capacity // user_bandwidth

# سوال 2: Packet Switching
def avg_bandwidth_packet_user(user_bandwidth=20, activity_ratio=0.2):
    return user_bandwidth * activity_ratio

def total_avg_bandwidth_packet(n_users, user_bandwidth=20, activity_ratio=0.2):
    return n_users * avg_bandwidth_packet_user(user_bandwidth, activity_ratio)

# سوال 3: احتمال ارسال فقط کاربر اول
def prob_only_user1_sending(n_users=19, p_send=0.2):
    return p_send * (1 - p_send) ** (n_users - 1)

# سوال 4: کسری مصرف لینک توسط یک کاربر
def link_fraction_used(user_bandwidth=20, link_capacity=200):
    return user_bandwidth / link_capacity

# سوال 5: احتمال بیش از 10 کاربر هم‌زمان ارسال کنند
def prob_more_than_k_sending(n_users=19, p_send=0.2, k=10):
    return 1 - binom.cdf(k, n_users, p_send)

# سوال 6: تأخیر لینک‌ها
def link_delays(L_bits=12000, rates=[10e6, 100e6, 1e6], lengths=[3000, 1000, 500000], c=3e8):
    trans_delays = [L_bits / r for r in rates]
    prop_delays = [d / c for d in lengths]
    total_delay = sum(trans_delays) + sum(prop_delays)
    return round(total_delay * 1000, 2)  # ms

# سوال 7: مدل Car-Caravan
def car_caravan_delay(N=10, toll_distance=75, car_speed=175, service_time=12):
    trans_delay = 3 * N * service_time
    prop_delay = 2 * (toll_distance / car_speed * 3600)
    return round(trans_delay + prop_delay, 2)  # seconds

# سوال 8: صف‌بندی
def avg_queue_delay(N, L, R):
    return ((N - 1) / 2) * (L / R)

def avg_queue_delay_equal_rate():
    return 0

# اجرای کدها
print("سوال 1: حداکثر کاربران circuit switching:", max_users_circuit_switching())
print("سوال 2: مصرف کل packet switching برای 19 کاربر:", total_avg_bandwidth_packet(19), "Mbps")
print("سوال 3: احتمال ارسال فقط کاربر اول:", round(prob_only_user1_sending(), 4))
print("سوال 4: کسری مصرف لینک توسط یک کاربر:", link_fraction_used())
print("سوال 5: احتمال بیش از 10 کاربر هم‌زمان ارسال:", round(prob_more_than_k_sending(), 4))
print("سوال 6: مجموع تأخیر سه لینک:", link_delays(), "ms")
print("سوال 7: تأخیر مدل کاروان:", car_caravan_delay(), "ثانیه")
print("سوال 8 (الف): میانگین تأخیر صف برای 87 بسته:", avg_queue_delay(87, 12000, 1e6), "ثانیه")
print("سوال 8 (ب): میانگین تأخیر صف در حالت نرخ برابر:", avg_queue_delay_equal_rate(), "ثانیه")