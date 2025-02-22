# Generated by Django 4.1.7 on 2023-04-09 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("reservations", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ExpertiseTV",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("invoice", models.BooleanField()),
                ("box", models.BooleanField()),
                ("guarantee_term", models.IntegerField()),
                ("guarantee_term_type", models.CharField(max_length=50)),
                ("color", models.CharField(max_length=50)),
                ("smart_tv", models.BooleanField()),
                ("panel_technology", models.CharField(max_length=50)),
                ("curved_screen", models.BooleanField()),
                ("os_type", models.CharField(max_length=50)),
                ("internal_satellite_receiver", models.BooleanField()),
                ("screen_size", models.IntegerField()),
                ("ambilight", models.BooleanField()),
                ("hdr", models.BooleanField()),
                ("full_array", models.BooleanField()),
                ("screen_resolution", models.CharField(max_length=50)),
                ("refresh_rate", models.IntegerField()),
                ("release_year", models.IntegerField()),
                ("screen_share", models.BooleanField()),
                ("wifi", models.BooleanField()),
                ("rf_input", models.BooleanField()),
                ("lan", models.BooleanField()),
                ("headphone_jack", models.BooleanField()),
                ("bluetooth", models.BooleanField()),
                ("hdmi", models.BooleanField()),
                ("usb", models.BooleanField()),
                ("is_screen_has_obscuration_problem", models.BooleanField()),
                ("is_screen_has_dead_pixel_problem", models.BooleanField()),
                ("is_screen_has_broken_problem", models.BooleanField()),
                ("is_screen_has_downfall_problem", models.BooleanField()),
                ("is_screen_has_band_problem", models.BooleanField()),
                ("is_screen_has_freezing_problem", models.BooleanField()),
                ("is_device_has_high_heat_problem", models.BooleanField()),
                ("is_device_has_sound_problem", models.BooleanField()),
                ("is_device_has_internal_receiver_problem", models.BooleanField()),
                ("is_device_has_speaker_problem", models.BooleanField()),
                ("is_screen_share_has_problem", models.BooleanField()),
                ("is_wifi_has_problem", models.BooleanField()),
                ("is_rf_input_has_problem", models.BooleanField()),
                ("is_ethernet_has_problem", models.BooleanField()),
                ("is_headphone_jack_has_problem", models.BooleanField()),
                ("is_bluetooth_has_problem", models.BooleanField()),
                ("is_hdmi_has_problem", models.BooleanField()),
                ("is_usb_has_problem", models.BooleanField()),
                ("is_remote_control_has_problem", models.BooleanField()),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("updated_date", models.DateTimeField(auto_now=True)),
                (
                    "reservation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="expertise_tv",
                        to="reservations.reservation",
                    ),
                ),
            ],
        ),
    ]
