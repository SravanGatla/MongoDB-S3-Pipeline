resource "aws_s3_bucket" "b" {
  bucket = "my-unique-tf-test-bucket001"

  versioning {
    enabled = true
  }

  tags = {
    Name = "My Bucket"
    Environment = "Dev"
  }
}
