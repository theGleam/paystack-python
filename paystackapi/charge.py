"""Script used to define the paystack Charge class."""

from paystackapi.base import PayStackBase


class Charge(PayStackBase):
    """docstring for Charge."""

    @classmethod
    def charge(cls, **kwargs):
        """
        Start a charge.

        Args:
            email: Customer's email address
            amount: Amount in kobo

        Returns:
            Json data from paystack API.
        """
        return cls().requests.post('charge', data=kwargs,)

    @classmethod
    def submit_pin(cls, **kwargs):
        """
        Submit PIN to continue a charge.

        Args:
            pin: PIN submitted by user
            reference: reference for transaction that requested pin

        Returns:
            Json data from paystack API.
        """
        return cls().requests.post('charge', data=kwargs,)

    @classmethod
    def submit_pin(cls, **kwargs):
        """
        Submit PIN to continue a charge.

        Args:
            pin: PIN submitted by user
            reference: reference for transaction that requested pin

        Returns:
            Json data from paystack API.
        """
        return cls().requests.post('charge/submit_pin', data=kwargs,)

    @classmethod
    def submit_otp(cls, **kwargs):
        """
        Submit OTP to complete a charge.

        Args:
            otp: OTP submitted by user
            reference: reference for ongoing transaction

        Returns:
            Json data from paystack API.
        """
        return cls().requests.post('charge/submit_otp', data=kwargs,)
    
    @classmethod
    def submit_phone(cls, **kwargs):
        """
        Submit Phone when requested.

        Args:
            phone: Phone submitted by user
            reference: reference for ongoing transaction

        Returns:
            Json data from paystack API.
        """
        return cls().requests.post('charge/submit_phone', data=kwargs,)
